Name:           puias-release
Version:        6
Release:        1.R
Summary:        PUIAS Linux repository

Group:          System Environment/Base
License:        BSD
URL:            http://puias.org
Source0:        RPM-GPG-KEY-puias
Source1:        puias-addons.repo
Source2:        puias-computational.repo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       system-release >= %{version}

# If apt is around, it needs to be a version with repomd support
Conflicts:      apt < 0.5.15lorg3

%description
PUIAS Linux repository. A project of members of the computing staff of
Princeton University and the Institute for Advanced Study. 

The Addons repository contains additional packages not included in a stock
Red Hat distribution. The Computational repository also includes additional
packages, however, these packages are specific to scientific computing.

Russian Fedora (%{repo}) Repository ConfiguratioeRussian Fedora (%{repo}) Repository Configuratio "Nothing to prep"

%build
echo "Nothing to build"

%install
rm -rf $RPM_BUILD_ROOT

# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

# Yum .repo files
%{__install} -p -m644 %{SOURCE1} %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%changelog
* Fri Jan 20 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 6-1.R
- initial build for EL
