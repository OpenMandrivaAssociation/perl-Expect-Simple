%define realname   Expect-Simple

Name:		perl-%{realname}
Version:    0.03
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perl wrapper around the Expect module  
Source0:    http://search.cpan.org/CPAN/authors/id/D/DJ/DJERIUS/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRequires:	perl-devel perl-Expect 
BuildArch:      noarch

%description
Expect::Simple is a wrapper around the Expect module which should suffice for 
simple applications. It hides most of the Expect machinery; the Expect object 
is available for tweaking if need be.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

