Summary:	HDF 4.x to/from HDF5 conversion tools
Summary(pl.UTF-8):	Narzędzia do konwersji pomiędzy HDF 4.x i HDF5
Name:		h4h5tools
Version:	2.2.4
Release:	1
Group:		Applications/File
License:	BSD-like, changed sources must be marked
Source0:	https://support.hdfgroup.org/ftp/HDF5/releases/tools/h4toh5/h4toh5-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	a1f3dd2882d890f40454782fa50d077d
Patch0:		%{name}-config.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-hdfeos.patch
Patch3:		%{name}-format.patch
URL:		http://www.hdfgroup.org/h4toh5/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	hdf-devel >= 4.2.6
BuildRequires:	hdf-eos-devel >= 2.17
BuildRequires:	hdf5-devel >= 1.6.10
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libtool
BuildRequires:	zlib-devel >= 1.1.3
Obsoletes:	hdf5-hdf4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities to convert files from HDF 4.x to HDF5 or from HDF5 to HDF
4.x format.

%description -l pl.UTF-8
Narzędzia do konwersji plików z formatu HDF 4.x do HDF5 oraz z HDF5 do
HDF 4.x.

%package lib
Summary:	HDF 4.x to/from HDF5 conversion library
Summary(pl.UTF-8):	Biblioteka do konwersji pomiędzy HDF 4.x i HDF5
Group:		Development/Libraries
Requires:	hdf >= 4.2.6
Requires:	hdf-eos >= 2.17
Requires:	hdf5 >= 1.6.10

%description lib
Library for file convertion from HDF 4.x to HDF5 or from HDF5 to HDF
4.x format.

%description lib -l pl.UTF-8
Biblioteka do konwersji plików z formatu HDF 4.x do HDF5 oraz z HDF5
do HDF 4.x.

%package devel
Summary:	Header files for HDF 4.x to/from HDF5 conversion library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki konwersji pomiędzy HDF 4.x i HDF5
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	hdf-devel >= 4.2.6
Requires:	hdf-eos-devel >= 2.17
Requires:	hdf5-devel >= 1.6.10

%description devel
Header files and documentation for HDF 4.x to/from HDF5 format
conversion library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do biblioteki konwersji plików z
formatu HDF 4.x do HDF5 i odwrotnie.

%package static
Summary:	Static HDF 4.x to/from HDF5 conversion library
Summary(pl.UTF-8):	Biblioteka statyczna do konwersji pomiędzy HDF 4.x i HDF5
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description static
Static library for file convertion from HDF 4.x to HDF5 or from HDF5
to HDF 4.x format.

%description static -l pl.UTF-8
Biblioteka statyczna do konwersji plików z formatu HDF 4.x do HDF5
oraz z HDF5 do HDF 4.x.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/hdf -DH5_USE_16_API"
%configure \
	--with-hdfeos2

%{__make} \
	h5toh4_LDADD="-lmfhdf"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING release_docs/{HISTORY,RELEASE}.txt
%attr(755,root,root) %{_bindir}/h4toh5
%attr(755,root,root) %{_bindir}/h5toh4

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libh4toh5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libh4toh5.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libh4toh5.so
%{_libdir}/libh4toh5.la
%{_includedir}/H4TOH5api_adpt.h
%{_includedir}/h4toh5*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libh4toh5.a
