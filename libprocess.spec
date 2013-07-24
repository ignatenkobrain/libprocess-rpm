%define commit 5ade0ea5807f3feef337f2e0ef7b773f57385ff6
%define shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           libprocess
Version:        0.0.1
Release:        2.%{shortcommit}%{?dist}
Summary:        Library that provides an actor style message-passing programming model (in C++)
License:        ASL 2.0
URL:            https://github.com/3rdparty/libprocess
#Source0:        https://github.com/3rdparty/libprocess/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# Temporary our fork
Source0:        https://github.com/ignatenkobrain/libprocess/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  zlib-devel
# TODO: Drop bundled packages
BuildRequires:  http-parser-devel
BuildRequires:  boost-devel
BuildRequires:  glog-devel
BuildRequires:  gtest-devel
BuildRequires:  gperftools-devel
BuildRequires:  libev-devel
BuildRequires:  protobuf-devel
BuildRequires:  stout-devel

%description
Library that provides an actor style message-passing programming model (in C++).

%prep
%setup -qn %{name}-%{commit}

%build
./bootstrap
%configure
make %{?_smp_mflags}

%check
make check

%install
rm -rf %{buildroot}
%make_install 

%files
%defattr(-,root,root,-)
%doc

%changelog
* Wed Jul 24 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-2.5ade0ea
- Enabled all BuildRequires
- Dropped most all bundled

* Tue Jul 23 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.0-1.f0d47da
- Initial release
