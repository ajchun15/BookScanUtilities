"""
깃 블로그에서 포스팅하는데 사용했던 MD 파일들을 하나로 이어붙이는 매우 짧은 개인용 유틸리티입니다.
여러 MD 파일을 한번에 단일의 PDF 파일로 쉽게 만들기 위해서 사용합니다.
"""
import os

input_path = os.getcwd()
output_file_name = "convert.md"

output_file = open(output_file_name, 'w');

"""
FSM의 구조
0--->("title" 감지: 쓰기)---> 1 --("--- 감지: \n<\hr>\n 쓰기")--> 2
무시                        무시                                 무시X
"""

for file in os.listdir(input_path):
    if file.endswith(".md") and file != "convert.md":
        input_file = open(file, "r", encoding="UTF-8");
        state = 0
        while True:
            line = input_file.readline()
            if not line:
                break
            
            if state == 0 and line.find("title") != -1:
                output_file.write("\n<hr/>\n")
                output_file.write("\n<hr/>\n")
                output_file.write("# "+ line[6:])
                state = 1
            elif state == 1 and line.find("---") != -1:
                output_file.write("\n<hr/>\n")
                output_file.write("\n<hr/>\n")
                state = 2
            elif state == 2:
                output_file.write(line)
            


        input_file.close()
        output_file.write('\n');
output_file.close()
        

