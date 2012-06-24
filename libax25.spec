# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	ax25 libraries for hamradio applications
Summary(pl.UTF-8):   Biblioteki ax25 dla aplikacji hamradio
Name:		libax25
Version:	0.0.11
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ax25/%{name}-%{version}.tar.gz
# Source0-md5:	c6ea01e81118451e2e892e634c576c17
URL:		http://ax25.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir		/var/lib

%description
These libraries are used for applications that need to get to some
special structures used in hamradio.

%description -l pl.UTF-8
Te biblioteki są potrzebne aby uruchamiać programy dla radioamatorów.

%package devel
Summary:	ax25 libraries development files
Summary(pl.UTF-8):   Pliki dla programistów używających bibliotek ax25
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The extra files needed to compile hamradio utilities.

%description devel -l pl.UTF-8
Dodatkowe pliki potrzebne do kompilacji programów dla radioamatorów.

%package static
Summary:	ax25 static libraries
Summary(pl.UTF-8):   Biblioteki statyczne ax25
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
ax25 static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne ax25.

%prep
%setup -q

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
%dir %{_localstatedir}/ax25
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libax25*.la
%attr(755,root,root) %{_libdir}/libax25*.so
%{_mandir}/man3/*
%{_includedir}/netax25/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libax25*.a
%endif
