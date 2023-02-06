import datetime
import time
import os
import subprocess

# ------------------------------------------------
username = ''  # 스트리머 ID
quality = 'best'  # 녹화 품질
root_path = r''  # 저장 경로
period = 10  # 반복 대기 시간 (초)
# ------------------------------------------------


def main():
    processed_path = os.path.join(root_path, username)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %Hh%Mm%Ss')
        filename = ''.join(x for x in f'{username} - {now}.ts' if x.isalnum() or x in ' -_.')
        recorded_filename = os.path.join(processed_path, filename)
        if not os.path.isdir(processed_path):
            os.makedirs(processed_path)
        subprocess.call(['streamlink', '--stream-segment-threads', '5', '--stream-segment-attempts', '5',
                         '--stream-segment-timeout', '20.0', '--hls-live-restart', '--twitch-disable-hosting',
                         '--twitch-disable-ads', 'twitch.tv/' + username, quality, '-o', recorded_filename])
        print(f"{username} 녹화 종료/실패. 오프라인 상태입니다.")
        print(f"{period}초 후에 다시 시도합니다.")
        time.sleep(period)


if __name__ == "__main__":
    main()

