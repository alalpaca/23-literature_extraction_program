from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        image_path = f"{output_folder}/page_{i + 1}.png"
        image.save(image_path, "PNG")
        print(f"已保存 {image_path}")

if __name__ == "__main__":
    pdf_path = "input.pdf"  # 替换为您的PDF文件路径（详细路径）
    output_folder = "output_images"  # 替换为保存输出图像的文件夹路径(不用详细路径)
    pdf_to_images(pdf_path, output_folder)

