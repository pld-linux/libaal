%define		snapshot	2003.12.23
%define		_snap	%(echo %{snapshot} | tr -d .)

Summary:	Library for Reiser4 filesystem
Summary(pl):	Bibloteka dla systemu plik�w Reiser4
Name:		libaal
Version:	0.4.15
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.namesys.com/snapshots/%{snapshot}/%{name}-%{version}.tar.gz
# Source0-md5:	bff755d94bf590c6c2cf8ae46e496b73
Patch0:		%{name}-opt.patch
Patch1:		%{name}-am18.patch
URL:		http://www.namesys.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libaal library - needed for Reiser4 filesystem utilities.

%description -l pl
Biblioteka libaal - potrzebna do narz�dzi dla systemu plik�w Reiser4.

%package devel
Summary:	Header files for libaal library
Summary(pl):	Pliki nag�owkowe biblioteki libaal
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libaal library.

%description devel -l pl
Pliki nag�owkowe biblioteki libaal.

%package static
Summary:	Static version of libaal
Summary(pl):	Wersja statyczna libaal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libaal library.

%description static -l pl
Statyczna wersja biblioteki libaal.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
