%global commit      d283d260937c8e7fc3a5fb4ffdbdef9f21688a50
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libprocess
Version:        0.0.1
Release:        11.%{shortcommit}%{?dist}
Summary:        Library that provides an actor style message-passing programming model (in C++)
License:        ASL 2.0
URL:            https://github.com/3rdparty/libprocess
Group:          System Environment/Libraries

Source0:        https://github.com/ignatenkobrain/libprocess/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  http-parser-devel
BuildRequires:  boost-devel
BuildRequires:  glog-devel
BuildRequires:  gmock-devel
BuildRequires:  gperftools-devel
BuildRequires:  libev-devel
BuildRequires:  protobuf-devel
BuildRequires:  stout-devel

%description
Library that provides an actor style message-passing programming model (in C++).

%package devel
Summary:        Header files for libprocess development
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for libprocess.

%prep
%setup -q -n %{name}-%{commit}

%build
./bootstrap
%configure --disable-static
make %{?_smp_mflags}

%check
make check ||:

%install
%make_install 

# Remove cruft
rm -f %{buildroot}%{_libdir}/libprocess.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libprocess.so.*
%doc LICENSE README

%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/libprocess/
%{_libdir}/libprocess.so

%changelog
* Tue Oct 1 2013 Timothy St. Clair <tstclair@redhat.com> - 0.0.1-11.d283d26
- Fixes from packaging review

* Mon Sep 16 2013 Timothy St. Clair <tstclair@redhat.com> - 0.0.1-10.4405209
- DISABLE tests that require DNS and fail in Koji.

* Fri Sep 6 2013 Timothy St. Clair <tstclair@redhat.com> - 0.0.1-9.bc412ff
- Cleanup from package review

* Wed Sep 4 2013 Timothy St. Clair <tstclair@redhat.com> - 0.0.1-8.56080c4
- Update from upstream 

* Fri Aug 16 2013 Timothy St. Clair <tstclair@redhat.com> - 0.0.1-7.ca0718f 
- Merge out from upstream mesos repo

* Fri Aug  9 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-7.35f872f
- Update to latest

* Tue Aug 6 2013 Timothy St. Clair <tstclair@redhat.com> - 0.0.1-6.35f872f
- Update to latest with merge in from upstream.

* Thu Aug  1 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-5.b29bd67
- Update to latest (with fix problems in http-parser)
- Some fixes in spec

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

* Tue Jul 23 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-1.f0d47da
- Initial release
