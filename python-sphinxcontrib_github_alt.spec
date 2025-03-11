#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Link to GitHub issues, pull requests, commits and users from Sphinx docs
Summary(pl.UTF-8):	Odnośniki z dokumentacji Sphinksa do zgłoszeń, pull requestów, commitów i użytkowników na GitHubie
Name:		python-sphinxcontrib_github_alt
Version:	1.1
Release:	8
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib_github_alt/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib_github_alt/sphinxcontrib_github_alt-%{version}.tar.gz
# Source0-md5:	6e8b239b13ee076c518446a101aa2f43
URL:		https://pypi.org/project/sphinxcontrib_github_alt/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-docutils
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Link to GitHub issues, pull requests, commits and users for a
particular project.

%description -l pl.UTF-8
Odnośniki z dokumentacji Sphinksa do zgłoszeń, pull requestów,
commitów i użytkowników na GitHubie.

%package -n python3-sphinxcontrib_github_alt
Summary:	Link to GitHub issues, pull requests, commits and users from Sphinx docs
Summary(pl.UTF-8):	Odnośniki z dokumentacji Sphinksa do zgłoszeń, pull requestów, commitów i użytkowników na GitHubie
Group:		Libraries/Python
Requires:	python3-docutils
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinxcontrib_github_alt
Link to GitHub issues, pull requests, commits and users for a
particular project.

%description -n python3-sphinxcontrib_github_alt -l pl.UTF-8
Odnośniki z dokumentacji Sphinksa do zgłoszeń, pull requestów,
commitów i użytkowników na GitHubie.

%prep
%setup -q -n sphinxcontrib_github_alt-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc COPYING.md README.rst
%{py_sitescriptdir}/sphinxcontrib_github_alt.py[co]
%{py_sitescriptdir}/sphinxcontrib_github_alt-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinxcontrib_github_alt
%defattr(644,root,root,755)
%doc COPYING.md README.rst
%{py3_sitescriptdir}/sphinxcontrib_github_alt.py
%{py3_sitescriptdir}/__pycache__/sphinxcontrib_github_alt.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_github_alt-%{version}-py*.egg-info
%endif
