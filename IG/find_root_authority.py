import os

def search_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                # 파일 접근 권한 확인
                file_stat = os.stat(filepath)
                # 파일 검색
                if file_stat.st_uid == 0:
                    print(f"Foud root file: {filepath}")
            except PermissionError:
                # 접근 불가능한 파일인 경우 스킵
                continue
            except Exception as e:
                print(f"An error occurred while searching {filepath}: {e}")

# 루트 디렉토리 설정
root_dir = "/home/kali"
# 검색 시작
search_files(root_dir)
