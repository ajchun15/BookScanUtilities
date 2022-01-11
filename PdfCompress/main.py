import pdf_to_image
import image_to_pdf
'''
#Main Routine
input_paths = []
pdf_names = []
environment = Environment(".jpg", 1, 30)

while True:
    print("Baramsil 이미지 자동 PDF 포장기 1.0.0")
    print("[현재 설정]")
    print("PDF내부이미지타입: {0} ".format(environment.output_type))
    print("경로목록--------------------------------------------------------")
    for directory in input_paths:
        print(directory)
    print("---------------------------------------------------------------")
    print("폴더 경로를 입력해주세요. 경로 입력을 끝마쳤다면 \"start\"를 입력해주세요. 출력 pdf의 이름은 폴더명을 따릅니다.")
    input_path = input()
    os.system("cls")

    if input_path == "start":
        break
    
    if not os.path.isdir(input_path):
        print("[오류]: 존재하지 않는 경로나 폴더 명입니다. 작업리스트에 추가할 수 없습니다.")
    elif has_dupliated_pdf_name(input_path, input_paths):
        print("[오류]: 폴더 명이 중복됩니다. 서로 같은 폴더명은 작업리스트에 추가할 수 없습니다.")
    else:
        input_paths.append(input_path)

print("변환을 시작합니다.")

for input_path in input_paths:
        print("{0}의 이미지 변환(->{1})을 시작합니다.".format(input_path, environment.output_type))
        convertImage(environment, input_path)
        print("{0}의 이미지 변환이 완료되었습니다. pdf로의 변환을 시작합니다.".format(input_path))
        convertToPdf(environment, input_path)


print("모든 변환을 끝마쳤습니다. 최종결과물은 프로그램이 있는 폴더에 저장되었습니다.")

'''

if __name__ == "__main__":
    environment = image_to_pdf.Environment(".jpg", 1, 50)
    #폴더에서 파일을 다 긁어오거나(pdf) 파일을 가져옴.
    #중간 경유지 역할을 하는 output 폴더를 만듬.
    #폴더에서 파일을 다 긁어옴(tiff)
    #pdf로 변환함.
    pdf_name = "CD, W11, 클라우드 데브옵스.pdf"
    pdf_to_image.convert_pdf_to_image(pdf_name, 6)
    image_to_pdf.convertImage(environment, "./temp")
    image_to_pdf.convertToPdf(environment, "./temp")
    
    
