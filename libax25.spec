#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	ax25 libraries for hamradio applications
Summary(pl.UTF-8):	Biblioteki ax25 dla aplikacji hamradio
Name:		libax25
Version:	0.0.11
Release:	5
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/ax25/%{name}-%{version}.tar.gz
# Source0-md5:	c6ea01e81118451e2e892e634c576c17
Patch0:		libadd.patch
URL:		http://ax25.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir		/var/lib

%description
These libraries are used for applications that need to get to some
special structures used in hamradio.

%description -l pl.UTF-8
Te biblioteki są wykorzystywane przez aplikacje wymagające specjalnych
struktur używanych przez urządzenia hamradio.

%package devel
Summary:	ax25 libraries development files
Summary(pl.UTF-8):	Pliki dla programistów używających bibliotek ax25
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibc-devel >= 2.1
Requires:	zlib-devel

%description devel
The extra files needed to compile hamradio utilities.

%description devel -l pl.UTF-8
Dodatkowe pliki potrzebne do kompilacji programów dla radioamatorów.

%package static
Summary:	ax25 static libraries
Summary(pl.UTF-8):	Biblioteki statyczne ax25
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
ax25 static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne ax25.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/ax25

%{__make} install installconf \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libax25.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libax25.so.0
%attr(755,root,root) %{_libdir}/libax25io.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libax25io.so.0
%dir %{_sysconfdir}/ax25
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/axports
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/nrports
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/rsports
%dir %{_localstatedir}/ax25
%{_mandir}/man5/axports.5*
%{_mandir}/man5/nrports.5*
%{_mandir}/man5/rsports.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libax25.so
%attr(755,root,root) %{_libdir}/libax25io.so
%{_libdir}/libax25.la
%{_libdir}/libax25io.la
%{_includedir}/netax25/*.h
%{_mandir}/man3/ax25.3*
%{_mandir}/man3/rose.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libax25.a
%{_libdir}/libax25io.a
%endif
