Summary: ax25 libraries for hamradio applications.
Name: libax25
Version: 0.0.9
Release: 1
License: LGPL
Group: Applications/Communications
Group(pl): Aplikacje/Komunikacja
Source0: ftp://sunsite.icm.edu.pl/vol/rzm1/linux-debian/pool/main/liba/libax25/libax25_%{version}.orig.tar.gz
BuildRoot: /tmp/%{name}-%{version}-root
ExclusiveArch: %{ix86}

%description

These libraries are used for applications that need to get to some
special structures used in hamradio.

%description -l pl

Te biblioteki sa potrzebne aby odpalic programy dla radioamatorow.

%package devel
Summary: ax25 library development files.
Group: Applications/Communications

%description devel
The extra files needed to compile hamradio utilities.

%description devel -l pl

Dodatkowe pliki potrzebne do kompilacji programow dla radioamatorow.

%prep
%setup -q

%build

%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/var/ax25

make DESTDIR=${RPM_BUILD_ROOT} install installconf

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README Changelog INSTALL COPYING

%dir			%{_sysconfdir}/ax25
%config(noreplace)	%{_sysconfdir}/ax25/axports
%config(noreplace)	%{_sysconfdir}/ax25/nrports
%config(noreplace)	%{_sysconfdir}/ax25/rsports

%dir			%{_localstatedir}/ax25

%{_libdir}/libax25*.so.*
%{_mandir}/man[35]/*

%files devel
%defattr(-,root,root)
%{_libdir}/libax25*.a
%{_libdir}/libax25*.la
%{_libdir}/libax25*.so

%{_includedir}/netax25
