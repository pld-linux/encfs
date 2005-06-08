Summary:	Encrypted pass-thru filesystem for Linux
Summary(pl):	Zaszyfrowany system plik�w dla Linuksa
Name:		encfs
Version:	1.2.2
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://arg0.net/users/vgough/download/%{name}-%{version}-2.tgz
# Source0-md5:	10a7fd97006a2b2f4f0347cd85048204
URL:		http://arg0.net/users/vgough/encfs.html
BuildRequires:	libfuse-devel >= 2.2
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	rlog-devel
Requires:	fusermount > 2.2
Requires:	rlog >= 1.3
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EncFS implements an encrypted filesystem in userspace using FUSE. FUSE
provides a Linux kernel module which allows virtual filesystems to be
written in userspace. EncFS encrypts all data and filenames in the
filesystem and passes access through to the underlying filesystem.
Similar to CFS except that it does not use NFS.

%description -l pl
EncFS jest implementacj� zaszyfrowanego systemu plik�w w przestrzeni
u�ytkownika przy u�yciu FUSE. FUSE dostarcza modu� j�dra Linuksa
pozwalaj�cy na obs�ug� wirtualnych system�w plik�w w przestrzeni
u�ytkownika. EncFS szyfruje wszystkie dane oraz nazwy plik�w w
systemie plik�w i przekazuje kontrol� do le��cego ni�ej systemu
plik�w. Jest podobny do CFS-a, ale nie u�ywa NFS-a.

%prep
%setup -q

%build
%configure \
	--enable-debug=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,adm) %{_bindir}/encfs*
%{_mandir}/man1/*.1*
