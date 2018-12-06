%global goipath    github.com/jfrogdev/gofrog
%global forgeurl   https://github.com/JFrogDev/gofrog/
%global commit     ff0e25ec116c8e43e9b697f162d63d3277c71ee1
Version: 0

%global common_description %{expand:
This is a collection of Go utilities written by JFrog developers.}

%gometa

Name:           %{goname}
Release:        0.2%{?dist}
Summary:        A collection of Go utilities by JFrog
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
BuildRequires:  golang(github.com/pkg/errors)

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitff0e25e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Dominik Mierzejewski <dominik.mierzejewski@citi.com> - 0-0.1.20180330gitff0e25e
- First package for Fedora
