%global debug_package %{nil}
%global gem_name bindata
Summary:        BinData - Parsing Binary Data in Ruby
Name:           rubygem-%{gem_name}
Version:        2.4.10
Release:        1%{?dist}
License:        BSD
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/dmendel/bindata
Source0:        https://github.com/dmendel/bindata/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
Patch0:         fix-file_list.patch
BuildRequires:  git
BuildRequires:  ruby
Requires:       ruby(release)
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
BinData provides a declarative way to read and write structured binary data.

This means the programmer specifies what the format of the binary data is, and BinData works out how to read and write data in this format. It is an easier (and more readable) alternative to ruby's #pack and #unpack methods.

BinData makes it easy to create new data types. It supports all the common primitive datatypes that are found in structured binary data formats. Support for dependent and variable length fields is built in.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem

%files
%defattr(-,root,root,-)
%doc %{gemdir}/gems/%{gem_name}-%{version}/BSDL
%{gemdir}

%changelog
* Mon Jun 13 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 2.4.10-1
- License verified
- Original version for CBL-Mariner
