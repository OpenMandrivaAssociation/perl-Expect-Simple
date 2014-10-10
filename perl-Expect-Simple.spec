%define upstream_name    Expect-Simple
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl wrapper around the Expect module  
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DJ/DJERIUS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Expect)
BuildArch:	noarch

%description
Expect::Simple is a wrapper around the Expect module which should suffice for 
simple applications. It hides most of the Expect machinery; the Expect object 
is available for tweaking if need be.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 405962
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2009.0
+ Revision: 268505
- rebuild early 2009.0 package (before pixel changes)

* Sat May 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
+ Revision: 205395
- update to new version 0.04

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.03-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.0
+ Revision: 69241
- update to new version 0.03


* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 0.02-2mdk
- Do not ship empty dir

* Sat Sep 24 2005 Michael Scherer <misc@mandriva.org> 0.02-1mdk
- First mandriva package

