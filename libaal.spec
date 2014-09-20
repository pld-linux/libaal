#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Library for Reiser4 filesystem
Summary(pl.UTF-8):	Bibloteka dla systemu plików Reiser4
Name:		libaal
Version:	1.0.6
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/reiser4/reiser4-utils/reiser4progs/%{name}-%{version}.tar.gz
# Source0-md5:	6fd5c2471e1fd3972fb23ac5dc1b77e3
Patch0:		%{name}-opt.patch
URL:		http://www.namesys.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libaal library - needed for Reiser4 filesystem utilities.

%description -l pl.UTF-8
Biblioteka libaal - potrzebna do narzędzi dla systemu plików Reiser4.

%package devel
Summary:	Header files for libaal library
Summary(pl.UTF-8):	Pliki nagłowkowe biblioteki libaal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libaal library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libaal.

%package static
Summary:	Static version of libaal
Summary(pl.UTF-8):	Wersja statyczna libaal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libaal library.

%description static -l pl.UTF-8
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
	%{!?debug:--disable-debug} \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# don't run ldconfig on install
> run-ldconfig
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libaal-*.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libaal-1.0.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libaal.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libaal-minimal.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libaal-minimal.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains information other than GPL text
%doc AUTHORS BUGS COPYING CREDITS ChangeLog README THANKS TODO
%attr(755,root,root) /%{_lib}/libaal-1.0.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libaal-1.0.so.6
%attr(755,root,root) /%{_lib}/libaal-minimal.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libaal-minimal.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaal.so
%attr(755,root,root) %{_libdir}/libaal-minimal.so
%{_libdir}/libaal.la
%{_libdir}/libaal-minimal.la
%{_includedir}/aal
%{_aclocaldir}/libaal.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libaal.a
%{_libdir}/libaal-minimal.a
%endif
