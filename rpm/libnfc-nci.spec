Name:           libnfc-nci
Version:        0.1.0
Release:        1
License:        Apache 2.0
Summary:        NFC stack for NXP
Url:            https://github.com/NXPNFCLinux/linux_libnfc-nci
Source0:        %{name}-%{version}.tar.bz2
Group:          System/Libraries
BuildRequires:  automake
BuildRequires:  libtool

%description
Linux NFC stack for NCI based NXP NFC Controllers

%package devel
Summary:        (development files)
Group:          Development/Libraries
Requires:       pkgconfig
Requires:       libnfc-nci = %{version}

%description devel
Linux NFC stack for NCI based NXP NFC Controllers (development files)

%package utils
Summary:        utilities
Group:          Applications/Text
Requires:       libnfc-nci >= %{version}

%description utils
Test application for NXP NFC.

%prep
%setup -q -n %{name}-%{version}/libnfc-nci

%build
mkdir -p m4
autoreconf -vfi %configure \
  --enable-shared \
  --disable-static \

make %{?_smp_mflags}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libnfc_nci_linux.so
%{_libdir}/libnfc_nci_linux-1.so
%config /etc/libnfc-nci.conf
%config /etc/libnfc-nxp-init.conf
%config /etc/libnfc-nxp-pn547.conf
%config /etc/libnfc-nxp-pn548.conf

%files devel
%defattr(-,root,root,-)
/usr/include/linux_nfc_api.h
/usr/include/linux_nfc_factory_api.h
%{_libdir}/pkgconfig/libnfc-nci.pc

%files utils
%defattr(-,root,root,-)
/usr/sbin/nfcDemoApp

