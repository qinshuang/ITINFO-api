#! /bin/bash
# =================================
# Example: 
# sh ObfuscatePy.sh src "manage.py" src 
#
#
# =================================

VERSION="1.0"
CURRENT_PATH=`pwd`
relative_path=$1
ENTRY=$2
PROJECT_NAME=$3

cd $relative_path
PROJECT_SRC_PATH=`pwd`
cd -

# =================================

other_file(){
cd ..
cp setup.py sdist/dist/
cp MANIFEST.in sdist/dist/
cp README.md sdist/dist/

for f in  logging.yml
do
cp $PROJECT_SRC_PATH/$f sdist/dist/$PROJECT_NAME
done
cd ..
cp setup.py sdist/dist/
cp MANIFEST.in sdist/dist/
cp README.md sdist/dist/
cd -
}

initLicense(){
cd sdist
echo $PROJECT_SRC_PATH
./pyarmor licenses --bind-file="$PROJECT_SRC_PATH/logging.yml;logging.yml" user
md5sum licenses/user/license.lic
cp licenses/user/license.lic dist/$PROJECT_NAME/license.lic
}

checkPyarmorInstall(){
if [ `pip list | grep pyarmor | wc -l` -eq 0 ] 
then
  pip install pyarmor
else 
  echo "Pyarmor already installed"
fi
}

obfuscate(){
pyarmor init --src=$PROJECT_SRC_PATH sdist
cd sdist
./pyarmor config --entry=$ENTRY --manifest="include *.py,recursive-include app *.py"
./pyarmor build
}


main(){
checkPyarmorInstall
obfuscate
other_file
initLicense
cd $CURRENT_PATH
}

main
