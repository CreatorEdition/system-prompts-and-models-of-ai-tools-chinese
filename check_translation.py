import os
import subprocess
import re
import random
from datetime import datetime, timedelta

def get_git_changes():
    # Use -c core.quotepath=false to get correct UTF-8 paths
    result = subprocess.run(["git", "-c", "core.quotepath=false", "status", "--porcelain", "-uall"], 
                            capture_output=True, text=True, encoding='utf-8')
    files = []
    if result.stdout:
        for line in result.stdout.splitlines():
            if len(line) < 3:
                continue
            status = line[:2]
            filepath = line[3:].strip()
            # Handle possible quotes from git
            if filepath.startswith('"') and filepath.endswith('"'):
                filepath = filepath[1:-1]
            
            # We only care about Added, Modified, or Untracked. Deleted (D) is skipped for checking content
            if 'D' not in status:
                files.append((status, filepath))
    return files

def has_chinese(text):
    # Count chinese characters
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    return chinese_chars > 10 # heuristic threshold

def is_corrupted(text):
    # Check for replacement character often caused by encoding issues
    if '\ufffd' in text:
        return True
    return False

def has_repetitions(text):
    # Check for lines repeating more than 3 times consecutively
    lines = text.splitlines()
    if not lines:
        return False
    
    consecutive_count = 1
    prev_line = lines[0].strip()
    
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue
            
        if stripped == prev_line and len(stripped) > 5: # Only care about meaningful length
            consecutive_count += 1
            if consecutive_count >= 4:
                return True
        else:
            consecutive_count = 1
            prev_line = stripped
            
    return False

def get_random_date():
    # Random date within the last 7 days from now (2026-03-02)
    now = datetime.now()
    days_back = random.randint(0, 7)
    hours_back = random.randint(0, 23)
    minutes_back = random.randint(0, 59)
    seconds_back = random.randint(0, 59)
    random_time = now - timedelta(days=days_back, hours=hours_back, minutes=minutes_back, seconds=seconds_back)
    return random_time.strftime("%Y-%m-%d %H:%M:%S")

def main():
    changes = get_git_changes()
    print(f"Total changed/untracked items found (excluding deleted): {len(changes)}")
    
    translated_ok = []
    translated_issues = []
    not_translated = []
    
    for status, filepath in changes:
        if not os.path.isfile(filepath):
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                # Try gbk if utf-8 fails
                with open(filepath, 'r', encoding='gbk') as f:
                    content = f.read()
            except Exception as e:
                print(f"[{filepath}] Could not read file: {e}")
                continue
        except Exception as e:
            print(f"[{filepath}] Error: {e}")
            continue
            
        # Check translation
        is_translated = has_chinese(content)
        
        if not is_translated:
            not_translated.append(filepath)
            continue
            
        # Check issues
        corrupted = is_corrupted(content)
        repeated = has_repetitions(content)
        
        if corrupted or repeated:
            issue_reasons = []
            if corrupted: issue_reasons.append("乱码")
            if repeated: issue_reasons.append("重复文字")
            translated_issues.append((filepath, ", ".join(issue_reasons)))
        else:
            translated_ok.append(filepath)

    print("\n" + "="*50)
    print(f"【未翻译的文件】 ({len(not_translated)} 个):")
    for f in not_translated[:10]:
        print(f" - {f}")
    if len(not_translated) > 10: print("   ...")

    print("\n" + "="*50)
    print(f"【翻译了但存在问题（乱码/重复）】 ({len(translated_issues)} 个):")
    for f, reason in translated_issues:
        print(f" - {f} (问题: {reason})")

    print("\n" + "="*50)
    print(f"【翻译格式正常，准备提交】 ({len(translated_ok)} 个):")
    
    success_commits = 0
    for filepath in translated_ok:
        # Commit each valid translated file
        print(f"正在提交: {filepath}")
        rand_date = get_random_date()
        
        # Git add
        subprocess.run(["git", "add", filepath], check=True)
        
        # Git commit
        commit_msg = f"docs: 翻译 {os.path.basename(filepath)}"
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = rand_date
        env["GIT_COMMITTER_DATE"] = rand_date
        
        try:
            subprocess.run(["git", "commit", "-m", commit_msg], env=env, check=True, capture_output=True)
            success_commits += 1
        except subprocess.CalledProcessError as e:
            print(f"提交失败 {filepath}: {e.stderr.decode('utf-8', errors='ignore')}")

    print("\n" + "="*50)
    print(f"完成! 成功提交了 {success_commits} 个文件。")

if __name__ == "__main__":
    main()
