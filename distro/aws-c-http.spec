Name:           aws-c-http
Version:        0.6.8 
Release:        6%{?dist}
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-http-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-compression-devel
BuildRequires:  aws-c-io-devel

Requires:       aws-c-common-libs
Requires:       aws-c-compression-libs
Requires:       aws-c-io-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
C99 implementation of the HTTP/1.1 and HTTP/2 specifications


%package libs
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications

%description libs
C99 implementation of the HTTP/1.1 and HTTP/2 specifications


%package devel
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
C99 implementation of the HTTP/1.1 and HTTP/2 specifications


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files
%{_bindir}/elasticurl

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libaws-c-http.so.1.0.0

%files devel
%dir %{_includedir}/aws/http
%{_includedir}/aws/http/*.h

%dir %{_libdir}/cmake/aws-c-http
%dir %{_libdir}/cmake/aws-c-http/shared
%{_libdir}/libaws-c-http.so
%{_libdir}/cmake/aws-c-http/aws-c-http-config.cmake
%{_libdir}/cmake/aws-c-http/shared/aws-c-http-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-http/shared/aws-c-http-targets.cmake


%changelog
* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.6.8-6
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.8-5
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.8-4
- Move elasticurl executable to standard package

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.8-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.6.8-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.8-1
- Initial package development
