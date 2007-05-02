# TODO: duplicated locales (es vs es_ES, fr vs fr_FR)
Summary:	Encrypted pass-thru filesystem for Linux
Summary(pl.UTF-8):	Zaszyfrowany system plików dla Linuksa
Name:		encfs
Version:	1.3.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://arg0.net/users/vgough/download/%{name}-%{version}-1.tgz
# Source0-md5:	c93d6a22aa858db4eb3803170a82274a
URL:		http://arg0.net/users/vgough/encfs.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.5
BuildRequires:	libstdc++-devel
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
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
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
