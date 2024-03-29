Summary:	X extension library
Name:		xorg-libXext
Version:	1.3.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
# Source0-md5:	52df7c4c1f0badd9f82ab124fb32eb97
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-proto >= 7.7
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X extension library.

%package devel
Summary:	Header files for libXext library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X extension library.

This package contains the header files needed to develop programs that
use libXext.

%prep
%setup -qn libXext-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-specs=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXext.so.?
%attr(755,root,root) %{_libdir}/libXext.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXext.so
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xext.pc
%{_mandir}/man3/*.3x*

