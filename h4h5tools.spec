Summary:	HDF 4.x to/from HDF5 conversion tools
Summary(pl.UTF-8):   Narzędzia do konwersji pomiędzy HDF 4.x i HDF5
Name:		h4h5tools
Version:	1.2
Release:	1
Group:		Applications/File
License:	Nearly BSD, but changed sources must be marked
Source0:	ftp://ftp.ncsa.uiuc.edu/HDF/HDF5/h4toh5/src/%{name}-%{version}.tar.gz
# Source0-md5:	a57c720f464956fbe3a730def01c9781
Source1:	http://hdf.ncsa.uiuc.edu/h4toh5/h4toh5lib_UG.pdf
# Source1-md5:	59dbe83604d64bcca35145899456c96e
Source2:	http://hdf.ncsa.uiuc.edu/h4toh5/h4toh5lib_RM.pdf
# Source2-md5:	dd9e2ca98a87e5f808b67ba5767b07ef
Patch0:		%{name}-config.patch
Patch1:		%{name}-shared.patch
URL:		http://hdf.ncsa.uiuc.edu/h4toh5/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	hdf-devel >= 4.0
BuildRequires:	hdf5-devel
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
Summary(pl.UTF-8):   Biblioteka do konwersji pomiędzy HDF 4.x i HDF5
Group:		Development/Libraries

%description lib
Library for file convertion from HDF 4.x to HDF5 or from HDF5 to HDF
4.x format.

%description lib -l pl.UTF-8
Biblioteka do konwersji plików z formatu HDF 4.x do HDF5 oraz z HDF5
do HDF 4.x.

%package devel
Summary:	Header files for HDF 4.x to/from HDF5 conversion library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki konwersji pomiędzy HDF 4.x i HDF5
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	hdf-devel
Requires:	hdf5-devel

%description devel
Header files and documentation for HDF 4.x to/from HDF5 format
conversion library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do biblioteki konwersji plików z
formatu HDF 4.x do HDF5 i odwrotnie.

%package static
Summary:	Static HDF 4.x to/from HDF5 conversion library
Summary(pl.UTF-8):   Biblioteka statyczna do konwersji pomiędzy HDF 4.x i HDF5
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

install %{SOURCE1} %{SOURCE2} .

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/hdf"
%configure

%{__make} \
	libh4toh5_la_LIBADD="-lmfhdf" \
	h5toh4_LDADD="-lmfhdf"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

find doc -name Dependencies -o -name Makefile\* | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING release_docs/release.txt
%attr(755,root,root) %{_bindir}/h4toh5
%attr(755,root,root) %{_bindir}/h5toh4

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc h4toh5lib_UG.pdf h4toh5lib_RM.pdf
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
