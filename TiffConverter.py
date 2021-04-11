import os
import img2pdf
import errno
from PIL import Image, ImageFilter
import shutil
import multiprocessing
outpath1 = 'C:\\Users\\MCOM\\Documents\\TestSpace'

#환경설정을 저장해두는 클래스입니다.
class Environment:
    def __init__(self, output_type, multiprocessing_num, jpg_quality):
        self.output_type = output_type #확장자 타입 jpg 또는 png
        self.multiprocessing_num = multiprocessing_num #병렬 실행 숫자.
        self.extension_dictionary = [".jpg", ".jpeg", ".png", ".tif"]
        self.jpg_quality = jpg_quality

# 폴더 명이 중복되는지 확인합니다. PDF 파일이 폴더명을 기반으로 생기기 때문에
# PDF 명이 중복된다면, PDF 파일들이 서로를 덮어쓰는 현상이 발생합니다.
def has_dupliated_pdf_name(input_path, paths):
    input_path_pdf = get_pdf_name(input_path)
    flag = False
    for path in paths:
        comparision_pdf = get_pdf_name(path)
        if input_path_pdf == comparision_pdf:
            flag = True
    return flag

#디렉터리 정보를 기반으로 PDF의 이름을 형성합니다.
def get_pdf_name(input_path):
    return input_path.split("\\")[-1]  + ".pdf"

#이미지를 변환합니다. Tiff->Jpg 변환은 90%의 용량압축 효율을 가지고 있습니다.
#변환된 이미지들은 해당 경로의 Convert 폴더에 저장됩니다.
def convertImage(environment: Environment, input_path):
    out_type = environment.output_type
    directory_name = input_path + "\\Convert"
    try:
        if not(os.path.isdir(directory_name)):
            os.makedirs(os.path.join(directory_name))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("오류: 디렉터리 생성 실패")
            raise

    for file in os.listdir(input_path):
        #파일 확장자 검사.
        is_correct_extension = False
        for extension in environment.extension_dictionary:
            if file.endswith(extension):
                is_correct_extension = True      
        if not is_correct_extension:
            continue
        
        #이미지 파일 변환 후 저장.
        with Image.open(input_path + "\\" + file) as im:
            if environment.output_type == ".jpg":
                back = Image.new("RGB", im.size, (255, 255, 255))
                back.paste(im)
                back.save(input_path + "\\Convert\\" + file + '.jpg', "JPEG", quality=environment.jpg_quality)
            elif environment.output_type == ".png":
                im.save(input_path + "\\Convert\\" + file + '.png')
            else:
                pass
            print("{0}의 이미지 변환을 수행중입니다....".format(input_path))
            print("변환중인 파일: {0}, 변환 포맷: {1}".format(file, out_type))

#Convert 폴더의 변환된 이미지들을 통해서 PDF를 생성합니다.
#PDF 변환이 완료된 후 Convert 폴더는 삭제됩니다.
def convertToPdf(enviroment: Environment, input_path):

    convert_path = input_path + "\\Convert"
    output_file_name = get_pdf_name(input_path)
    with open(output_file_name, "wb") as f:
        pdf_list = []

        for file in os.listdir(convert_path):
            if enviroment.output_type == ".jpg" and file.endswith(".jpg"):
                pdf_list.append(convert_path + "\\" + file)
            elif enviroment.output_type == ".png" and file.endswith(".png"):
                pdf_list.append(convert_path + "\\" + file)
            else:
                pass

        pdf = img2pdf.convert(*pdf_list)
        f.write(pdf)

        shutil.rmtree(convert_path)


#Main Routine
input_paths = []
pdf_names = []
environment = Environment(".jpg", 1, 70)

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
