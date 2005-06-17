# TODO: duplicated locales (es vs es_ES, fr vs fr_FR)
Summary:	Encrypted pass-thru filesystem for Linux
Summary(pl):	Zaszyfrowany system plików dla Linuksa
Name:		encfs
Version:	1.2.2
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://arg0.net/users/vgough/download/%{name}-%{version}-2.tgz
# Source0-md5:	10a7fd97006a2b2f4f0347cd85048204
URL:		http://arg0.net/users/vgough/encfs.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	rlog-devel
Requires:	rlog >= 1.3
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EncFS implements an encrypted filesystem in userspace using FUSE. FUSE
provides a Linux kernel module which allows virtual filesystems to be
written in userspace. EncFS encrypts all data and filenames in the
filesystem and passes access through to the underlying filesystem.
Similar to CFS except that it does not use NFS.

%description -l pl
EncFS jest implementacj± zaszyfrowanego systemu plików w przestrzeni
u¿ytkownika przy u¿yciu FUSE. FUSE dostarcza modu³ j±dra Linuksa
pozwalaj±cy na obs³ugê wirtualnych systemów plików w przestrzeni
u¿ytkownika. EncFS szyfruje wszystkie dane oraz nazwy plików w
systemie plików i przekazuje kontrolê do le¿±cego ni¿ej systemu
plików. Jest podobny do CFS-a, ale nie u¿ywa NFS-a.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-debug=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# No public headers => no need for devel files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/encfs*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*.1*
