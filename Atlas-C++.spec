Summary:	C++ reference implementation of the Atlas protocol
Summary(pl):	Implementacja protoko�u Atlas
Name:		Atlas-C++
Version:	0.4.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://victor.worldforge.org/pub/worldforge/libs/Atlas-C++/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atlas-C++ is the current C++ implementation of the Atlas protocol, a
communications layer designed to be used in the WorldForge MMORPG
gaming system. This library is suitable for linking to either clients
xor servers.

%description -l pl
Atlas-C++ jest implementacj� (w j�zyku C++) protoko�u Atlas, warstwy
komunikacyjnej przeznaczonej do system�w WorldForge MMORPG. Bibliotek�
t� przygotowano zar�wno dla aplikacji klienckich, jak i serwer�w.

%package devel
Summary:	Header files for Atlas-C++ development
Summary(pl):	Pliki nag��wkowe do biblioteki Atlas-C++
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
Atlas-C++ is the current C++ implementation of the Atlas protocol, a
communications layer designed to be used in the WorldForge MMORPG
gaming system. This library is suitable for linking to either clients
or servers.

This package contains the header files needed to develop programs that
use these Atlas-C++

%description devel -l pl
Atlas-C++ jest implementacj� (w j�zyku C++) protoko�u Atlas, warstwy
komunikacyjnej przeznaczonej do system�w WorldForge MMORPG. Bibliotek�
t� przygotowano zar�wno dla aplikacji klienckich, jak i serwer�w.

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych bibliotek Atlas-C++.

%package static
Summary:	Static libraries for Atlas-C++ development
Summary(pl):	Statyczne biblioteki Atlas-C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Atlas-C++ is the current C++ implementation of the Atlas protocol, a
communications layer designed to be used in the WorldForge MMORPG
gaming system. This library is suitable for linking to either clients
or servers.

This package contains the static Atlas-C++ libraries.

%description static -l pl
Atlas-C++ jest implementacj� (w j�zyku C++) protoko�u Atlas, warstwy
komunikacyjnej przeznaczonej do system�w WorldForge MMORPG. Bibliotek�
t� przygotowano zar�wno dla aplikacji klienckich, jak i serwer�w.

Pakiet zawiera statyczne biblioteki Atlas-C++.

%prep
%setup -q

%build
aclocal
autoheader
libtoolize --automake --copy --force
automake --add-missing --copy --gnu --force
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atlas-config
%{_includedir}/Atlas
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_aclocaldir}/atlas.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
