
Name: app-subversion
Epoch: 1
Version: 1.6.5
Release: 1%{dist}
Summary: Subversion - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-subversion-%{version}.tar.gz
Buildarch: noarch

%description
Subversion server app.

%package core
Summary: Subversion - Core
Requires: app-base-core
Requires: app-storage-core
Requires: subversion

%description core
Subversion server app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/subversion
cp -r * %{buildroot}/usr/clearos/apps/subversion/

install -d -m 0755 %{buildroot}/var/clearos/subversion
install -d -m 0755 %{buildroot}/var/clearos/subversion/repositories
install -D -m 0644 packaging/subversion_default.conf %{buildroot}/etc/clearos/storage.d/subversion_default.conf

%post core
logger -p local6.notice -t installer 'app-subversion-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/subversion/deploy/install ] && /usr/clearos/apps/subversion/deploy/install
fi

[ -x /usr/clearos/apps/subversion/deploy/upgrade ] && /usr/clearos/apps/subversion/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-subversion-core - uninstalling'
    [ -x /usr/clearos/apps/subversion/deploy/uninstall ] && /usr/clearos/apps/subversion/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/subversion/packaging
%dir /usr/clearos/apps/subversion
%dir /var/clearos/subversion
%dir /var/clearos/subversion/repositories
/usr/clearos/apps/subversion/deploy
/usr/clearos/apps/subversion/language
/etc/clearos/storage.d/subversion_default.conf
