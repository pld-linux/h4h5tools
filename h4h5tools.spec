Summary:	HDF 4.x to/from HDF5 conversion tools
Summary(pl):	Narzêdzia do konwersji pomiêdzy HDF 4.x i HDF5
Name:		h4h5tools
Version:	1.0
Release:	2
Group:		Applications/File
License:	Nearly BSD, but changed sources must be marked
Source0:	ftp://ftp.ncsa.uiuc.edu/HDF/HDF5/h4toh5/src/%{name}.tar.gz
Source1:	http://hdf.ncsa.uiuc.edu/h4toh5/h4toh5lib_UG.pdf
Patch0:		%{name}-config.patch
URL:		http://hdf.ncsa.uiuc.edu/h4toh5/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	hdf-devel >= 4.0
BuildRequires:	hdf5-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libtool
BuildRequires:	zlib-devel >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	hdf5-hdf4

%description
Utilities to convert files from HDF 4.x to HDF5 or from HDF5 to HDF
4.x format.

%description -l pl
Narzêdzia do konwersji plików z formatu HDF 4.x do HDF5 oraz z HDF5 do
HDF 4.x.

%package lib
Summary:	HDF 4.x to/from HDF5 conversion library
Summary(pl):	Biblioteka do konwersji pomiêdzy HDF 4.x i HDF5
Group:		Development/Libraries

%description lib
Library for file convertion from HDF 4.x to HDF5 or from HDF5 to HDF
4.x format.

%description lib -l pl
Biblioteka do konwersji plików z formatu HDF 4.x do HDF5 oraz z HDF5
do HDF 4.x.

%package devel
Summary:	Header files for HDF 4.x to/from HDF5 conversion library
Summary(pl):	Pliki nag³ówkowe biblioteki konwersji pomiêdzy HDF 4.x i HDF5
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}

%description devel
Header files and documentation for HDF 4.x to/from HDF5 format
conversion library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki konwersji plików z
formatu HDF 4.x do HDF5 i odwrotnie.

%package static
Summary:	Static HDF 4.x to/from HDF5 conversion library
Summary(pl):	Biblioteka statyczna do konwersji pomiêdzy HDF 4.x i HDF5
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}

%description static
Static library for file convertion from HDF 4.x to HDF5 or from HDF5
to HDF 4.x format.

%description static -l pl
Biblioteka statyczna do konwersji plików z formatu HDF 4.x do HDF5
oraz z HDF5 do HDF 4.x.

%prep
%setup -q -n %{name}
%patch -p1
install %{SOURCE1} .

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-hdf4=%{_includedir}/hdf,%{_libdir}

%{__make}

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
%doc COPYING release_docs/{README,release.txt}
%attr(755,root,root) %{_bindir}/h4toh5
%attr(755,root,root) %{_bindir}/h5toh4

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc h4toh5lib_UG.pdf
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
