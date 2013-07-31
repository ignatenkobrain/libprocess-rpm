%global commit      d47b962a614ba3a86d7a4a428f2debfc02d5690b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libprocess
Version:        0.0.1
Release:        4.%{shortcommit}%{?dist}
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
BuildRequires:  http-parser-devel
BuildRequires:  boost-devel
BuildRequires:  glog-devel
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  gperftools-devel
BuildRequires:  libev-devel
BuildRequires:  protobuf-devel
BuildRequires:  stout-devel

%description
Library that provides an actor style message-passing programming model (in C++).

%package devel
Summary: Header files for libprocess development
Group: Development/Libraries
Requires: %name = %version-%release

%description devel
Header files for libprocess, a library that provides an actor style message-passing programming model (in C++)

%prep
%setup -qn %{name}-%{commit}

%build
./bootstrap
%configure
make %{?_smp_mflags}

%check
make check

%install
%make_install 

# Remove static libraries and libtool files
rm -f %{buildroot}%{_libdir}/libprocess.a
rm -f %{buildroot}%{_libdir}/libprocess.la
# Rename folder in include  dir
mv %{buildroot}%{_includedir}/process %{buildroot}%{_includedir}/libprocess

%files
%{_libdir}/libprocess.s*
%{_datadir}/pkgconfig/*
%doc LICENSE README

%files devel
%{_includedir}/libprocess/
%doc LICENSE README

%changelog
* Wed Jul 31 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-4.84ce2f3
- Add gmock-devel BR
- Fix files in devel
- Enable check
- Drop %%defattr

* Fri Jul 26 2013 Timothy St. Clair <tstclair@redhat.com> - 0.0.1-3.e93ab81
- Start contents packaging for libprocess 

* Wed Jul 24 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-2.5ade0ea
- Enabled all BuildRequires
- Dropped most all bundled

* Tue Jul 23 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.0-1.f0d47da
- Initial release
