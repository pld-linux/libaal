%define		snapshot	2003.05.28
%define		snap	%(echo %{snapshot} | tr -d .)

Summary:	Lib for Reiser4 filesystem
Summary(pl):	Bibloteka dla systemu plików Reiser4
Name:		libaal
Version:	0.4.5
Release:	%{snap}.1
License:	GPL v2
Group:		Libraries
# Source0-md5:	7310fcf9adadf7c6e11416e1c48f779d
Source0:	http://thebsh.namesys.com/snapshots/%{snapshot}/%{name}-%{snap}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
URL:		http://www.namesys.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl
Ta bibiloteka jest potrzebna je¿eli chcesz u¿ywaæ nowego systemu plików Resier4

%package static
Summary:        Static versionf of libaal
Summary(pl):    Wersja statyczna libaal
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description static
Static version of libaal.

%description static -l pl
Statyczna bibloteka libaal.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,5},%{_pkgconfigdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING CREDITS ChangeLog INSTALL NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/*%{version}*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.*a

%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
