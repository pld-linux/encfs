# TODO: duplicated locales (es vs es_ES, fr vs fr_FR)
Summary:	Encrypted pass-thru filesystem for Linux
Summary(pl.UTF-8):	Zaszyfrowany system plików dla Linuksa
Name:		encfs
Version:	1.7.4
Release:	8
License:	GPL v2
Group:		Applications/System
#Source0Download: http://www.arg0.net/encfs
Source0:	http://encfs.googlecode.com/files/%{name}-%{version}.tgz
# Source0-md5:	ac90cc10b2e9fc7e72765de88321d617
URL:		http://www.arg0.net/encfs
#BuildRequires:	autoconf >= 2.50
#BuildRequires:	automake
BuildRequires:	boost-devel >= 1.34.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	libfuse-devel >= 2.5
BuildRequires:	libstdc++-devel
#BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	rlog-devel >= 1.3
Requires:	rlog >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EncFS implements an encrypted filesystem in userspace using FUSE. FUSE
provides a Linux kernel module which allows virtual filesystems to be
written in userspace. EncFS encrypts all data and filenames in the
filesystem and passes access through to the underlying filesystem.
Similar to CFS except that it does not use NFS.

%description -l pl.UTF-8
EncFS jest implementacją zaszyfrowanego systemu plików w przestrzeni
użytkownika przy użyciu FUSE. FUSE dostarcza moduł jądra Linuksa
pozwalający na obsługę wirtualnych systemów plików w przestrzeni
użytkownika. EncFS szyfruje wszystkie dane oraz nazwy plików w
systemie plików i przekazuje kontrolę do leżącego niżej systemu
plików. Jest podobny do CFS-a, ale nie używa NFS-a.

%prep
%setup -q

%build
%configure \
	--with-boost-filesystem=boost_filesystem \
	--with-boost-serialization=boost_serialization \
	--with-boost-system=boost_system

%{__make} -j1 \
	LDFLAGS="-lboost_system"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# No public headers => no need for devel files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.{la,so}

# duplicate of de,es,fr,hu,pt
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{de_DE,es_ES,fr_FR,hu_HU,pt_PT}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/encfs
%attr(755,root,root) %{_bindir}/encfsctl
%attr(755,root,root) %{_bindir}/encfssh
%attr(755,root,root) %{_libdir}/libencfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libencfs.so.6
%{_mandir}/man1/encfs.1*
%{_mandir}/man1/encfsctl.1*
