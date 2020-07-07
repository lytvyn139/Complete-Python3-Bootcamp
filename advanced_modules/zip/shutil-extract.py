import shutil
dir_to_zip = '/home/coding/python/udemy/1/advanced_modules/zip/archive-me'

output_filename = 'shutil_zip'
# Just fill in the output_filename and the directory to zip
# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename,'zip',dir_to_zip)

# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive('shutil_zip.zip','shutil_unzip_folder','zip')