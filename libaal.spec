Summary:	Library for Reiser4 filesystem
Summary(pl):	Bibloteka dla systemu plików Reiser4
Name:		libaal
Version:	1.0.4
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.namesys.com/pub/reiser4progs/%{name}-%{version}.tar.gz
# Source0-md5:	bdcdb1b8ca13dba897c0a2138d1643f5
Patch0:		%{name}-opt.patch
URL:		http://www.namesys.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libaal library - needed for Reiser4 filesystem utilities.

%description -l pl
Biblioteka libaal - potrzebna do narzêdzi dla systemu plików Reiser4.

%package devel
Summary:	Header files for libaal library
Summary(pl):	Pliki nag³owkowe biblioteki libaal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libaal library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libaal.

%package static
Summary:	Static version of libaal
Summary(pl):	Wersja statyczna libaal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libaal library.

%description static -l pl
Statyczna wersja biblioteki libaal.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?debug:--disable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains information other than GPL text
%doc AUTHORS BUGS COPYING CREDITS ChangeLog README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
