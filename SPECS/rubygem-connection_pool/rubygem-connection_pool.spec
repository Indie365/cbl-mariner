%global debug_package %{nil}
%global gem_name connection_pool
Summary:        Generic connection pooling for Ruby
Name:           rubygem-%{gem_name}
Version:        2.2.5
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/mperham/connection_pool
Source0:        https://github.com/mperham/connection_pool/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
Patch0:         fix-file_list.patch
BuildRequires:  git
BuildRequires:  ruby
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
Generic connection pooling for Ruby
MongoDB has its own connection pool. ActiveRecord has its own connection pool. This is a generic connection pool that can be used with anything, e.g. Redis, Dalli and other Ruby network clients.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE
%{gemdir}

%changelog
* Mon Jun 13 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 2.2.5-1
- License verified
- Original version for CBL-Mariner
