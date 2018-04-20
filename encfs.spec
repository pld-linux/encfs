# TODO: duplicated locales (es vs es_ES, fr vs fr_FR)
%bcond_without	tests
Summary:	Encrypted pass-thru filesystem for Linux
Summary(pl.UTF-8):	Zaszyfrowany system plików dla Linuksa
Name:		encfs
Version:	1.9.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/vgough/encfs/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	28e6c0a9dbfb26b1e53f491bff4e707b
URL:		http://www.arg0.net/encfs
BuildRequires:	boost-devel >= 1.34.0
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	libfuse-devel >= 2.5
BuildRequires:	libstdc++-devel
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
install -d build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF

%{__make}

%if %{with tests}
%{__make} unittests
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicate of de,es,fr,hu,pt
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{de_DE,es_ES,fr_FR,pt_PT}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/encfs
%attr(755,root,root) %{_bindir}/encfsctl
%attr(755,root,root) %{_bindir}/encfssh
%{_mandir}/man1/encfs.1*
%{_mandir}/man1/encfsctl.1*
%{_mandir}/man1/encfssh.1*
