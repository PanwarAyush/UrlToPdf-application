from selenium import webdriver
import pdfkit
def fun(text):
 driver = webdriver.Edge()
 driver.get(text);

 # open new file
 file = open("myfile.html", "w")
 file.write("<!DOCTYPE html><html><head></head><body width=\"600px\">")

 # write image
 file.write("<img src=\"data:image/png;base64,")
 file.write(driver.get_screenshot_as_base64())
 file.write("\">")

# close file
 file.write("</body></html>")
 file.close()

 path_wkthmltopdf=b'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'  #can also be done via Envt. Settings in windows!
 config=pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
 pdfkit.from_file('myfile.html', 'out.pdf',configuration=config)
 driver.close()