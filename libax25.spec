# TODO: FHS (/var/ax25 -> /var/lib/ax25(?))
Summary:	ax25 libraries for hamradio applications
Summary(pl):	Biblioteki ax25 dla aplikacji hamradio
Name:		libax25
Version:	0.0.10
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ax25/%{name}-%{version}.tar.gz
URL:		http://ax25.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These libraries are used for applications that need to get to some
special structures used in hamradio.

%description -l pl
Te biblioteki s� potrzebne aby uruchamia� programy dla radioamator�w.

%package devel
Summary:	ax25 libraries development files
Summary(pl):	Pliki dla programist�w u�ywaj�cych bibliotek ax25
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The extra files needed to compile hamradio utilities.

%description devel -l pl
Dodatkowe pliki potrzebne do kompilacji program�w dla radioamator�w.

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
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}/var/ax25

%{__make} DESTDIR=${RPM_BUILD_ROOT} install installconf

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%dir %{_sysconfdir}/ax25
%config(noreplace) %{_sysconfdir}/ax25/axports
%config(noreplace) %{_sysconfdir}/ax25/nrports
%config(noreplace) %{_sysconfdir}/ax25/rsports
%attr(755,root,root) %{_libdir}/libax25*.so.*.*
# NOT FHS-compliant
%dir %{_localstatedir}/ax25
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libax25*.la
%attr(755,root,root) %{_libdir}/libax25*.so
%{_mandir}/man3/*
%{_includedir}/netax25/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libax25*.a