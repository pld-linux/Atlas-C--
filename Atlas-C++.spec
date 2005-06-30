Summary:	C++ reference implementation of the Atlas protocol
Summary(pl):	Implementacja protoko³u Atlas
Name:		Atlas-C++
Version:	0.4.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.worldforge.org/pub/worldforge/libs/Atlas-C++/%{name}-%{version}.tar.bz2
# Source0-md5:	5ef0a12001d3924baa2742171af31ed3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atlas-C++ is the current C++ implementation of the Atlas protocol, a
communications layer designed to be used in the WorldForge MMORPG
gaming system. This library is suitable for linking to either clients
xor servers.

%description -l pl
Atlas-C++ jest implementacj± (w jêzyku C++) protoko³u Atlas, warstwy
komunikacyjnej przeznaczonej do systemów WorldForge MMORPG. Bibliotekê
tê przygotowano zarówno dla aplikacji klienckich, jak i serwerów.

%package devel
Summary:	Header files for Atlas-C++ development
Summary(pl):	Pliki nag³ówkowe do biblioteki Atlas-C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Atlas-C++ is the current C++ implementation of the Atlas protocol, a
communications layer designed to be used in the WorldForge MMORPG
gaming system. This library is suitable for linking to either clients
or servers.

This package contains the header files needed to develop programs that
use these Atlas-C++

%description devel -l pl
Atlas-C++ jest implementacj± (w jêzyku C++) protoko³u Atlas, warstwy
komunikacyjnej przeznaczonej do systemów WorldForge MMORPG. Bibliotekê
tê przygotowano zarówno dla aplikacji klienckich, jak i serwerów.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych bibliotek Atlas-C++.

%package static
Summary:	Static libraries for Atlas-C++ development
Summary(pl):	Statyczne biblioteki Atlas-C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Atlas-C++ is the current C++ implementation of the Atlas protocol, a
communications layer designed to be used in the WorldForge MMORPG
gaming system. This library is suitable for linking to either clients
or servers.

This package contains the static Atlas-C++ libraries.

%description static -l pl
Atlas-C++ jest implementacj± (w jêzyku C++) protoko³u Atlas, warstwy
komunikacyjnej przeznaczonej do systemów WorldForge MMORPG. Bibliotekê
tê przygotowano zarówno dla aplikacji klienckich, jak i serwerów.

Pakiet zawiera statyczne biblioteki Atlas-C++.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/Atlas*
%{_aclocaldir}/atlas.m4
%{_pkgconfigdir}/atlascpp*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
