set -ex
PACKAGE_NAME=dep_package.tar.gz
CWD=`pwd`
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade -r requirements.txt -i
cd .venv/lib/python3*/site-packages/
tar cazf $CWD/$PACKAGE_NAME `ls | grep -ve "-\|.md\|pip\|wheel\|setuptools"`
cd $CWD
deactivate
rm -rf .venv
# prompt the user for input
echo "Enter the GCS path to push the dependency package tar.gz file: "
read gcs_path
gsutil -m cp $PACKAGE_NAME $gcs_path
rm $PACKAGE_NAME