set -e
PACKAGES=()
DO_INSTALL=0
if ! opkg list-installed | grep -F 'python36 - 3.6.4-r0'; then
    PACKAGES+=("opkg_cache/python36_3.6.4-r0_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "python36 already installed"
fi
if ! opkg list-installed | grep -F 'python36-robotpy-ctre - 2018.1.3'; then
    PACKAGES+=("opkg_cache/python36-robotpy-ctre_2018.1.3_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "python36-robotpy-ctre already installed"
fi
if [ "${DO_INSTALL}" == "0" ]; then
    echo "No packages to install."
else
    opkg install  ${PACKAGES[@]}
fi