echo ==== CREATING VFS COPY ====
echo ==== VFS VAULT TEST ====
ls
echo ==== VFS LV1 TEST ====
cd vfs_lv1
ls
echo ==== Return to vfs_vault ====
cd ..
ls
echo ==== VFS LV2 TEST ====
cd vfs_lv2
ls
echo ==== DOCS ====
cd docs
ls
echo ==== Return to vfs_vault ====
cd ..
cd ..
ls
echo ==== VFS LV3 TEST ====
cd vfs_lv3
ls
echo ==== FIRST LEVEL ====
cd level1
ls
echo ==== SECOND LEVEL ====
cd level2
ls
echo Trying cd into non-existent folder:
cd fake
echo ==== THIRD LEVEL ====
cd level3
ls
echo ==== Return to vfs_vault ====
cd ..
cd ..
cd ..
cd ..
ls
echo Trying "cd" without parameters:
cd