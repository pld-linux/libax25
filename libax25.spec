Summary:	ax25 libraries for hamradio applications
Summary(pl):	Biblioteki ax25 dla aplikacji hamradio
Name:		libax25
Version:	0.0.9
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://sunsite.icm.edu.pl/vol/rzm1/linux-debian/pool/main/liba/libax25/%{name}_%{version}.orig.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These libraries are used for applications that need to get to some
special structures used in hamradio.

%description -l pl
Te biblioteki s± potrzebne aby uruchamiaæ programy dla radioamatorów.

%package devel
Summary:	ax25 libraries development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych bibliotek ax25
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The extra files needed to compile hamradio utilities.

%description devel -l pl
Dodatkowe pliki potrzebne do kompilacji programów dla radioamatorów.

%package static
Summary:	ax25 static libraries
Summary(pl):	Biblioteki statyczne ax25
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
ax25 static libraries.

%description static -l pl
Biblioteki statyczne ax25.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}/var/ax25

%{__make} DESTDIR=${RPM_BUILD_ROOT} install installconf

gzip -9nf AUTHORS NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_sysconfdir}/ax25
%config(noreplace) %{_sysconfdir}/ax25/axports
%config(noreplace) %{_sysconfdir}/ax25/nrports
%config(noreplace) %{_sysconfdir}/ax25/rsports
%attr(755,root,root) %{_libdir}/libax25*.so.*.*
%dir %{_localstatedir}/ax25
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libax25*.la
%attr(755,root,root) %{_libdir}/libax25*.so
%{_mandir}/man3/*
%{_includedir}/netax25

%files static
%defattr(644,root,root,755)
%{_libdir}/libax25*.a
