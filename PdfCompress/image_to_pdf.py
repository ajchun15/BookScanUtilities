import os
import img2pdf
import errno
from PIL import Image, ImageFilter
import shutil
outpath1 = 'C:\\Users\\MCOM\\Documents\\TestSpace'

#환경설정을 저장해두는 클래스입니다.
class Environment:
    def __init__(self, output_type, multiprocessing_num, jpg_quality):
        self.output_type = output_type #확장자 타입 jpg 또는 png
        self.multiprocessing_num = multiprocessing_num #병렬 실행 숫자.
        self.extension_dictionary = [".jpg", ".jpeg", ".png", ".tif", "tiff"]
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


