%define debug_package %{nil}

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-luassert
Version:        1.7.10
Release:        1%{?dist}
Summary:        Lua Assertions Extension

License:        MIT
URL:            https://github.com/Olivine-Labs/luassert
Source0:        https://github.com/Olivine-Labs/luassert/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif

Requires:       lua-say

%description
luassert extends Lua's built-in assertions to provide additional tests and the
ability to create your own. You can modify chains of assertions with 'not'.


%prep
%setup -q -n luassert-%{version}


%build


%install
install -d %{buildroot}%{luapkgdir}/
cp -ar src/ %{buildroot}%{luapkgdir}/luassert/


%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{luapkgdir}/luassert/


%changelog
* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.7.10-1
- Public release
