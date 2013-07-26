%define commit e93ab811055dd459a8eb53938a920dc05819219d
%define shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libprocess
Version:        0.0.1
Release:        3.%{shortcommit}%{?dist}
Summary:        Library that provides an actor style message-passing programming model (in C++)
License:        ASL 2.0
URL:            https://github.com/3rdparty/libprocess
Group:          System Environment/Libraries

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


%package devel
Summary: Headers for Condor's classified advertisement language
Group: Development/Libraries
Requires: %name = %version-%release

%description devel
Devel libraries for such and such


%prep
%setup -qn %{name}-%{commit}

%build
./bootstrap
%configure
make %{?_smp_mflags}

%check
# TODO: Needs revisit for cleaning.
# make check

%install
rm -rf %{buildroot}
%make_install 

#remove the static library elements?  I'm still debating.
rm -f %{buildroot}/%{_libdir}/libprocess.a
rm -f %{buildroot}/%{_libdir}/libprocess.la


%files
%defattr(-,root,root,-)
%{_libdir}/libprocess.s*
%{_datadir}/pkgconfig/*
%doc LICENSE README

%files devel
%defattr(-,root,root,-)
# this needs to be changed to {name}. 
%{_includedir}/process/
%doc LICENSE README

%changelog
* Fri Jul 26 2013 Timothy St. Clair <tstclair@redhat.com> - 0.0.1-3.e93ab81
- Start contents packaging for libprocess 

* Wed Jul 24 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-2.5ade0ea
- Enabled all BuildRequires
- Dropped most all bundled

* Tue Jul 23 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.0-1.f0d47da
- Initial release
