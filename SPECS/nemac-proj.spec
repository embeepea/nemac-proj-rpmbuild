Name:           nemac-proj
Version:        4.8.0
Release:        3%{?dist}
Summary:        NEMAC's custom build of proj4

Group:          Applications/Engineering
License:        GPLV2+
URL:            http://trac.osgeo.org/proj/
Source0:        proj-%{version}.tar.gz

%description
This is NEMAC's custom build of proj4 for use on servers.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n proj-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*
%{_mandir}/*



%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h

%changelog
