import pytesseract
import cv2
import re

def extract_bill_info(bill_image):
    image = cv2.imread(bill_image)
    text = pytesseract.image_to_string(image)

    bill_info = {}
    for line in text.split("\n"):
        match = re.search(r"Bill Number: (.*)", line)
        if match:
            bill_info["bill_number"] = match.group(1)
        match = re.search(r"Date: (.*)", line)
        if match:
            bill_info["date"] = match.group(1)
        match = re.search(r"Total Amount Due: (.*)", line)
        if match:
            bill_info["total_amount_due"] = match.group(1)
        match = re.search(r"Invoice Date: (.*)", line)
        if match:
            bill_info["invoice_date"] = match.group(1)
        match = re.search(r"Due Date: (.*)", line)
        if match:
            bill_info["due_date"] = match.group(1)
        match = re.search(r"Items: (.*)", line)
        if match:
            bill_info["items"] = match.group(1).split(", ")
        match = re.search(r"Price: (.*)", line)
        if match:
            bill_info["price"] = match.group(1)

    return bill_info

if __name__ == "__main__":
    bill_info = extract_bill_info("bill.jpg")
    print(bill_info)
