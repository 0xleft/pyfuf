# download from https://github.com/ffuf/ffuf/releases/download/v2.1.0/ffuf_2.1.0_windows_amd64.zip and https://github.com/ffuf/ffuf/releases/download/v2.1.0/ffuf_2.1.0_linux_amd64.tar.gz
# then unzip and untar then move to ./bin folder

set -e 

# download windows
mkdir ./temp
wget https://github.com/ffuf/ffuf/releases/download/v2.1.0/ffuf_2.1.0_windows_amd64.zip
unzip ffuf_2.1.0_windows_amd64.zip -d ./temp
mv ./temp/ffuf.exe ./bin/windows_fuff.exe
mv ./temp/LICENSE ./bin/LICENSE
mv ./temp/README.md ./bin/README.md
mv ./temp/CHANGELOG.md ./bin/CHANGELOG.md
rm -rf ./temp

# download linux
mkdir ./temp
wget https://github.com/ffuf/ffuf/releases/download/v2.1.0/ffuf_2.1.0_linux_amd64.tar.gz
tar -xvf ffuf_2.1.0_linux_amd64.tar.gz -C ./temp
mv ./temp/ffuf ./bin/linux_ffuf
rm -rf ./temp

# clean up
rm ffuf_2.1.0_windows_amd64.zip
rm ffuf_2.1.0_linux_amd64.tar.gz