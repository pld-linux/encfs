Summary:	Encrypted pass-thru filesystem for Linux
Name:		encfs
Version:	1.2.0
Release:	0.1
License:	GPL v2
Group:		System/Filesystems
######		Unknown group!
Source0:	http://arg0.net/users/vgough/download/%{name}-%{version}-2.tgz
# Source0-md5:	cc653aa2f6ad2f479a3b6d075d6eb43a
URL:		http://arg0.net/users/vgough/encfs.html
BuildRequires:	libfuse-devel >= 2.2
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	rlog >= 1.3
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EncFS implements an encrypted filesystem in userspace using FUSE. FUSE
provides a Linux kernel module which allows virtual filesystems to be
written in userspace. EncFS encrypts all data and filenames in the
filesystem and passes access through to the underlying filesystem.
Similar to CFS except that it does not use NFS.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
